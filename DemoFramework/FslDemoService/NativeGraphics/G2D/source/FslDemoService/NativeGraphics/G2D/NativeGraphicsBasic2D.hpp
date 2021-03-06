#ifndef FSLDEMOSERVICE_NATIVEGRAPHICS_G2D_NATIVEGRAPHICSBASIC2D_HPP
#define FSLDEMOSERVICE_NATIVEGRAPHICS_G2D_NATIVEGRAPHICSBASIC2D_HPP
/****************************************************************************************************************************************************
* Copyright (c) 2014 Freescale Semiconductor, Inc.
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*
*    * Redistributions of source code must retain the above copyright notice,
*      this list of conditions and the following disclaimer.
*
*    * Redistributions in binary form must reproduce the above copyright notice,
*      this list of conditions and the following disclaimer in the documentation
*      and/or other materials provided with the distribution.
*
*    * Neither the name of the Freescale Semiconductor, Inc. nor the names of
*      its contributors may be used to endorse or promote products derived from
*      this software without specific prior written permission.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
* ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
* WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
* IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
* INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
* BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
* DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
* LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
* OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
* ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*
****************************************************************************************************************************************************/

#include <FslDemoHost/Base/Service/NativeGraphics/INativeGraphicsBasic2D.hpp>

namespace Fsl
{
  namespace G2D
  {
    class NativeGraphicsBasic2D
      : public INativeGraphicsBasic2D
    {
      Point2 m_currentResolution;
      Point2 m_fontSize;
      bool m_inBegin;
    public:
      NativeGraphicsBasic2D(const Point2& currentResolution);
      ~NativeGraphicsBasic2D();

      // From INativeGraphicsBasic2D
      virtual void SetScreenResolution(const Point2& currentResolution) override;
      virtual void Begin() override;
      virtual void End() override;
      virtual void DrawPoints(const Vector2*const pDst, const uint32_t length, const Color& color) override;
      virtual void DrawString(const char*const characters, const uint32_t length, const Vector2& dstPosition) override;
      virtual Point2 FontSize() const override;
    private:
    };
  }
}

#endif
